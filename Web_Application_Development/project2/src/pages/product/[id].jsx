'use client';
import { useEffect, useState } from 'react';
import { useRouter } from 'next/router';
import api from '../../services/api';
import { Container, Row, Col, Button, Form, Badge } from 'react-bootstrap';
import NavigationBar from '../../components/NavigationBar';
import ReviewList from '../../components/ReviewList';
import AddReviewForm from '../../components/AddReviewForm';
import Link from 'next/link';

export default function ProductDetailPage() {
  const router = useRouter();
  const { id } = router.query;

  const [product, setProduct] = useState(null);
  const [campaign, setCampaign] = useState(null);
  const [quantity, setQuantity] = useState(1);
  const [total, setTotal] = useState(0);

  useEffect(() => {
    if (id) {
      api.get(`/products/${id}`)
        .then(res => setProduct(res.data))
        .catch(err => console.error(err));

      api.get('/campaigns')
        .then(res => {
          const match = res.data.find(c => 
            c.products && c.products.includes(id)
          );
          if (match) {
            setCampaign(match);
          }
        })
        .catch(err => console.error(err));
    }
  }, [id]);

  useEffect(() => {
    if (product) {
      const price = campaign
        ? product.price * (1 - (campaign.discountPercentage || 0) / 100)
        : product.price;
      setTotal(price * quantity);
    }
  }, [quantity, product, campaign]);

  const handleAddToCart = () => {
    if (!quantity || quantity < 1) return alert('Please select quantity');
    
    const item = {
      id: product.id,
      title: product.title,
      price: campaign 
        ? product.price * (1 - (campaign.discountPercentage || 0) / 100)
        : product.price,
      quantity
    };

    api.get(`/shoppingcart/${product.id}`)
      .then(() => api.put(`/shoppingcart/${product.id}`, item))
      .catch(() => api.post('/shoppingcart', item))
      .then(() => alert('Added to cart!'))
      .catch(err => console.error(err));
  };

  if (!product) return <div>Loading...</div>;

  const discountedPrice = campaign
    ? (product.price * (1 - (campaign.discountPercentage || 0) / 100)).toFixed(2)
    : product.price;

  return (
    <>
      <NavigationBar />
      <Container className="py-4">
        <Row>
          <Col md={6}>
            <img src={product.image} alt={product.title} className="img-fluid mb-3" />
          </Col>
          <Col md={6}>
            <h2>{product.title}</h2>
            {campaign && (
              <Badge bg="success" className="mb-2">{campaign.title}</Badge>
            )}
            <p>{product.description}</p>
            <p>
              {campaign ? (
                <>
                  <span className="text-muted text-decoration-line-through me-2">
                    {product.price}₺
                  </span>
                  <strong className="text-danger">{discountedPrice}₺</strong>
                  <span className="text-success ms-2">
                    (-{campaign.discountPercentage}%)
                  </span>
                </>
              ) : (
                <strong>{product.price}₺</strong>
              )}
            </p>

            <Form.Group controlId="quantity" className="mb-3">
              <Form.Label>Quantity</Form.Label>
              <Form.Control
                type="number"
                min="1"
                value={quantity}
                onChange={(e) => setQuantity(parseInt(e.target.value) || 1)}
              />
            </Form.Group>

            <h4>Total: {total.toFixed(2)}₺</h4>

            <Button variant="success" onClick={handleAddToCart}>Add to Cart</Button>{' '}
            <Link href="/cart" passHref>
              <Button variant="outline-primary" className="ms-2">Go to Cart</Button>
            </Link>
          </Col>
        </Row>

        <hr />

        <h3>Reviews</h3>
        <ReviewList productId={product.id} />

        <h4>Add Your Review</h4>
        <AddReviewForm productId={product.id} />
      </Container>
    </>
  );
}