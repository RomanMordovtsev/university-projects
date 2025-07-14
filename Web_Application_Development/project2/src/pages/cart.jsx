'use client';
import { useEffect, useState } from 'react';
import { Container, Table, Button, Form, Alert } from 'react-bootstrap';
import NavigationBar from '../components/NavigationBar';
import api from '../services/api';

export default function CartPage() {
  const [cart, setCart] = useState([]);
  const [notes, setNotes] = useState({});
  const [showSummary, setShowSummary] = useState(false);
  const [paid, setPaid] = useState(false);

  const fetchCart = () => {
    api.get('/shoppingcart')
      .then(res => setCart(res.data))
      .catch(err => console.error(err));
  };

  useEffect(() => {
    fetchCart();
  }, []);

  const handleQuantityChange = (id, quantity) => {
    const updated = cart.find(item => item.id === id);
    updated.quantity = quantity;
    api.put(`/shoppingcart/${id}`, updated)
      .then(fetchCart);
  };

  const handleDelete = (id) => {
    api.delete(`/shoppingcart/${id}`)
      .then(fetchCart);
  };

  const handleEmpty = () => {
    return Promise.all(cart.map(item => api.delete(`/shoppingcart/${item.id}`)))
      .then(fetchCart);
  };

  const handleNoteChange = (id, note) => {
    setNotes({ ...notes, [id]: note });
  };

  const handlePayment = () => {
    handleEmpty().then(() => {
      setPaid(true);
      setShowSummary(false);
    });
  };

  const totalPrice = cart.reduce((sum, item) => sum + item.quantity * item.price, 0);
  const delivery = totalPrice < 1000 ? 50 : 0;
  const totalWithDelivery = totalPrice + delivery;

  return (
    <>
      <NavigationBar />
      <Container className="py-4">
        <h2>Shopping Cart</h2>

        {paid && <Alert variant="success">Payment successful! Your order has been processed.</Alert>}

        {cart.length === 0 ? (
          <p>Your cart is empty.</p>
        ) : (
          <>
            <Table striped bordered hover>
              <thead>
                <tr>
                  <th>Title</th>
                  <th>Quantity</th>
                  <th>Note</th>
                  <th>Total</th>
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                {cart.map(item => (
                  <tr key={item.id}>
                    <td>{item.title}</td>
                    <td>
                      <Form.Control
                        type="number"
                        value={item.quantity}
                        min="1"
                        onChange={e => handleQuantityChange(item.id, parseInt(e.target.value))}
                      />
                    </td>
                    <td>
                      <Form.Control
                        type="text"
                        value={notes[item.id] || ''}
                        onChange={e => handleNoteChange(item.id, e.target.value)}
                      />
                    </td>
                    <td>{(item.quantity * item.price).toFixed(2)}₺</td>
                    <td>
                      <Button variant="danger" onClick={() => handleDelete(item.id)}>Remove</Button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </Table>

            {showSummary && (
              <Alert variant="info">
                <p><strong>Subtotal:</strong> {totalPrice.toFixed(2)}₺</p>
                <p><strong>Delivery:</strong> {delivery}₺</p>
                <p><strong>Total:</strong> {totalWithDelivery.toFixed(2)}₺</p>
              </Alert>
            )}

            <div className="d-flex justify-content-between mt-3">
              <Button variant="secondary" onClick={() => setShowSummary(!showSummary)}>
                {showSummary ? 'Hide Summary' : 'Show Summary'}
              </Button>
              <Button variant="success" onClick={handlePayment}>Pay Now</Button>
            </div>
          </>
        )}
      </Container>
    </>
  );
}
