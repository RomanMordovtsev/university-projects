'use client';
import { useState, useEffect } from 'react';
import { Container, Form, Button, Row, Col } from 'react-bootstrap';
import api from '../services/api';
import NavigationBar from '../components/NavigationBar';

export default function AddCampaign() {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [image, setImage] = useState('');
  const [productIds, setProductIds] = useState([]);
  const [allProducts, setAllProducts] = useState([]);

  useEffect(() => {
    api.get('/products')
      .then(res => setAllProducts(res.data))
      .catch(err => console.error(err));
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    const campaign = {
      title,
      description,
      image,
      products: productIds.map(Number)
    };

    api.post('/campaigns', campaign)
      .then(() => alert('Campaign created!'))
      .catch(err => console.error(err));
  };

  const toggleProduct = (id) => {
    setProductIds((prev) =>
      prev.includes(id) ? prev.filter((p) => p !== id) : [...prev, id]
    );
  };

  return (
    <>
      <NavigationBar />
      <Container className="py-4">
        <h2>Create New Campaign</h2>
        <Form onSubmit={handleSubmit}>
          <Form.Group className="mb-3">
            <Form.Label>Title</Form.Label>
            <Form.Control value={title} onChange={e => setTitle(e.target.value)} required />
          </Form.Group>

          <Form.Group className="mb-3">
            <Form.Label>Description</Form.Label>
            <Form.Control value={description} onChange={e => setDescription(e.target.value)} required />
          </Form.Group>

          <Form.Group className="mb-3">
            <Form.Label>Image URL</Form.Label>
            <Form.Control value={image} onChange={e => setImage(e.target.value)} required />
          </Form.Group>

          <Form.Group className="mb-3">
            <Form.Label>Products to Include</Form.Label>
            <Row>
              {allProducts.map((p) => (
                <Col md={6} key={p.id}>
                  <Form.Check
                    type="checkbox"
                    label={`${p.title}`}
                    checked={productIds.includes(p.id)}
                    onChange={() => toggleProduct(p.id)}
                  />
                </Col>
              ))}
            </Row>
          </Form.Group>

          <Button type="submit" variant="primary">Save Campaign</Button>
        </Form>
      </Container>
    </>
  );
}
