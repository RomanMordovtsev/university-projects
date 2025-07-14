'use client';
import { useEffect, useState } from 'react';
import { Carousel } from 'react-bootstrap';
import api from '../services/api';

const CampaignCarousel = () => {
  const [campaigns, setCampaigns] = useState([]);

  useEffect(() => {
    api.get('/campaigns')
      .then(response => setCampaigns(response.data))
      .catch(error => console.error('Error fetching campaigns:', error));
  }, []);

  return (
    <Carousel className="mb-4">
      {campaigns.map(campaign => (
        <Carousel.Item key={campaign.id}>
          <img
            className="d-block w-100"
            src={campaign.image}
            alt={campaign.title}
            style={{ maxHeight: '400px', objectFit: 'cover' }}
          />
          <Carousel.Caption>
            <h3>{campaign.title}</h3>
            <p>{campaign.description}</p>
          </Carousel.Caption>
        </Carousel.Item>
      ))}
    </Carousel>
  );
};

export default CampaignCarousel;
