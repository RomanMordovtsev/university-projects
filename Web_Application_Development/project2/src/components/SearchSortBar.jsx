'use client';
import { useState } from 'react';
import { Form, Row, Col } from 'react-bootstrap';

const SearchSortBar = ({ onSearchChange, onSortChange }) => {
  const [search, setSearch] = useState('');
  const [sort, setSort] = useState('');

  const handleSearchChange = (e) => {
    const value = e.target.value;
    setSearch(value);
    onSearchChange(value);
  };

  const handleSortChange = (e) => {
    const value = e.target.value;
    setSort(value);
    onSortChange(value);
  };

  return (
    <Row className="mb-4">
      <Col md={8}>
        <Form.Control
          type="text"
          placeholder="Search products..."
          value={search}
          onChange={handleSearchChange}
        />
      </Col>
      <Col md={4}>
        <Form.Select value={sort} onChange={handleSortChange}>
          <option value="">Sort By</option>
          <option value="priceAsc">Price: Low to High</option>
          <option value="priceDesc">Price: High to Low</option>
          <option value="titleAsc">Title: A-Z</option>
          <option value="titleDesc">Title: Z-A</option>
        </Form.Select>
      </Col>
    </Row>
  );
};

export default SearchSortBar;
