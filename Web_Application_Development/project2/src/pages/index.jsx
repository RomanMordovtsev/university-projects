'use client';
import NavigationBar from "../components/NavigationBar";
import CampaignCarousel from "../components/CampaignCarousel";
import SearchSortBar from "../components/SearchSortBar";
import ProductList from "../components/ProductList";
import { Container } from "react-bootstrap";
import { useState } from "react";
import api from "../services/api";

export default function Home() {
  const [searchQuery, setSearchQuery] = useState('');
  const [sortOption, setSortOption] = useState('');

  const handleAddToCart = (product) => {
    api.get(`/shoppingcart/${product.id}`)
      .then(res => {
        // If item exists in cart, update quantity
        const existingItem = res.data;
        const updatedItem = {
          ...existingItem,
          quantity: existingItem.quantity + 1
        };
        return api.put(`/shoppingcart/${product.id}`, updatedItem);
      })
      .catch(() => {
        // If item doesn't exist, add new item
        const newItem = {
          id: product.id,
          title: product.title,
          price: product.price,
          quantity: 1
        };
        return api.post('/shoppingcart', newItem);
      })
      .then(() => alert('Added to cart!'))
      .catch(err => console.error(err));
  };

  return (
    <>
      <NavigationBar />
      <Container>
        <CampaignCarousel />
        <SearchSortBar 
          onSearchChange={setSearchQuery}
          onSortChange={setSortOption}
        />
        <ProductList 
          searchQuery={searchQuery} 
          sortOption={sortOption}
          onAddToCart={handleAddToCart}
        />
      </Container>
    </>
  );
}