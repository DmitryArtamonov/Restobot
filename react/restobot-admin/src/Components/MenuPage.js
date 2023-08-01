import React, { useEffect, useState } from 'react';
import Dish from './Dish';
import '../styles.css';


const MenuPage = () => {
  const [dishes, setDishes] = useState([]);

  useEffect(() => {
    // Create an asynchronous function to perform the GET request
    async function fetchDishes() {
      try {
        // Await the completion of the GET request and get the response
        const response = await fetch('http://127.0.0.1:8000/api/dishes/1');
        const data = await response.json();
        // Update the 'dishes' state with the received data
        setDishes(data);
      } catch (error) {
        console.error('Error fetching dishes:', error);
      }
    }

    // Call the asynchronous function to perform the GET request
    fetchDishes();
  }, []);

  return (
    <div className="m-4">
      <h1>Dish List</h1>
      <div className="divide-y divide-gray-100 ">
        {dishes.map((dish) => (
          // Use the 'Dish' component for each dish
          <Dish key={dish.id} {...dish} />
        ))}
      </div>
    </div>
  );
};

export default MenuPage;