'use client';
import { useState } from 'react';
import { Form, Button } from 'react-bootstrap';
import api from '../services/api';

const AddReviewForm = ({ productId }) => {
  const [username, setUsername] = useState('');
  const [title, setTitle] = useState('');
  const [text, setText] = useState('');
  const [stars, setStars] = useState(5);

  const handleSubmit = (e) => {
    e.preventDefault();
    const review = {
      productId,
      username,
      title,
      text,
      stars
    };

    api.post('/reviews', review)
      .then(() => {
        alert('Review submitted!');
        setUsername('');
        setTitle('');
        setText('');
        setStars(5);
      })
      .catch(err => console.error(err));
  };

  return (
    <Form onSubmit={handleSubmit} className="mb-5">
      <Form.Group className="mb-3">
        <Form.Label>Your Name</Form.Label>
        <Form.Control value={username} onChange={e => setUsername(e.target.value)} required />
      </Form.Group>

      <Form.Group className="mb-3">
        <Form.Label>Review Title</Form.Label>
        <Form.Control value={title} onChange={e => setTitle(e.target.value)} required />
      </Form.Group>

      <Form.Group className="mb-3">
        <Form.Label>Review Text</Form.Label>
        <Form.Control as="textarea" rows={3} value={text} onChange={e => setText(e.target.value)} required />
      </Form.Group>

      <Form.Group className="mb-3">
        <Form.Label>Stars</Form.Label>
        <Form.Select value={stars} onChange={e => setStars(Number(e.target.value))}>
          {[1, 2, 3, 4, 5].map(num => (
            <option key={num} value={num}>{num}</option>
          ))}
        </Form.Select>
      </Form.Group>

      <Button type="submit" variant="primary">Submit Review</Button>
    </Form>
  );
};

export default AddReviewForm;
