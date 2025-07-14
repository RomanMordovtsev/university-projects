'use client';
import { Card, Button, Badge } from 'react-bootstrap';
import Link from 'next/link';

const ProductCard = ({ product, campaign, onAddToCart }) => {
  const hasCampaign = Boolean(campaign);
  const discount = hasCampaign && campaign.discountPercentage;
  const discountedPrice = discount
    ? (product.price * (1 - discount / 100)).toFixed(2)
    : null;

  return (
    <Card className="h-100">
      <Link href={`/product/${product.id}`} className="text-decoration-none text-dark">
        <Card.Img
          variant="top"
          src={product.image}
          style={{ height: '200px', objectFit: 'cover' }}
        />
        <Card.Body>
          {hasCampaign && (
            <Badge bg="success" className="mb-2">
              {campaign.title} (-{discount}%)
            </Badge>
          )}
          <Card.Title>{product.title}</Card.Title>
          <Card.Text>{product.description}</Card.Text>
          {discountedPrice ? (
            <Card.Text>
              <span style={{ textDecoration: 'line-through', color: 'gray' }}>
                {product.price}₺
              </span>{' '}
              <strong style={{ color: 'red' }}>{discountedPrice}₺</strong>
            </Card.Text>
          ) : (
            <Card.Text><strong>{product.price}₺</strong></Card.Text>
          )}
        </Card.Body>
      </Link>
      <Card.Footer className="bg-white border-top-0">
        <Button
          variant="primary"
          onClick={(e) => {
            e.preventDefault();
            onAddToCart(product);
          }}
        >
          Add to Cart
        </Button>
      </Card.Footer>
    </Card>
  );
};

export default ProductCard;