'use client';
import { useEffect, useState } from 'react';
import api from '../services/api';
import { ListGroup, Badge } from 'react-bootstrap';

const ReviewList = ({ productId }) => {
  const [reviews, setReviews] = useState([]);

  useEffect(() => {
    if (productId) {
      api.get(`/reviews?productId=${productId}`)
        .then(res => setReviews(res.data))
        .catch(err => console.error(err));
    }
  }, [productId]);

  if (reviews.length === 0) {
    return <p>No reviews yet.</p>;
  }

  return (
    <ListGroup className="mb-4">
      {reviews.map(review => (
        <ListGroup.Item key={review.id}>
          <h5>{review.title} <Badge bg="warning" text="dark">⭐ {review.stars}</Badge></h5>
          <p><em>by {review.username}</em></p>
          <p>{review.text}</p>
        </ListGroup.Item>
      ))}
    </ListGroup>
  );
};

export default ReviewList;
