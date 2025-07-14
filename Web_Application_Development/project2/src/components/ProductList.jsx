'use client';
import { useEffect, useState } from 'react';
import { Row, Col } from 'react-bootstrap';
import ProductCard from './ProductCard';
import api from '../services/api';

const ProductList = ({ searchQuery, sortOption, onAddToCart }) => {
  const [products, setProducts] = useState([]);
  const [campaigns, setCampaigns] = useState([]);

  useEffect(() => {
    api.get('/products')
      .then(res => setProducts(res.data))
      .catch(err => console.error(err));

    api.get('/campaigns')
      .then(res => setCampaigns(res.data))
      .catch(err => console.error(err));
  }, []);

  const filtered = products.filter(p =>
    p.title.toLowerCase().includes(searchQuery.toLowerCase())
  );

  const sorted = [...filtered].sort((a, b) => {
    switch (sortOption) {
      case 'priceAsc':
        return a.price - b.price;
      case 'priceDesc':
        return b.price - a.price;
      case 'titleAsc':
        return a.title.localeCompare(b.title);
      case 'titleDesc':
        return b.title.localeCompare(a.title);
      default:
        return 0;
    }
  });

  const getProductCampaign = (product) => {
    return campaigns.find(c => 
      c.products && c.products.includes(String(product.id))
    );
  };

  return (
    <Row xs={1} md={3} className="g-4">
      {sorted.map(product => {
        const campaign = getProductCampaign(product);
        return (
          <Col key={product.id}>
            <ProductCard
              product={product}
              campaign={campaign}
              onAddToCart={onAddToCart}
            />
          </Col>
        );
      })}
    </Row>
  );
};

export default ProductList;