import React, { useEffect, useState } from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import NavBar from "./NavBar";
import MainWindow from "./MainWindow";
import OrdersPage from "./OrdersPage";
import MenuPage from "./MenuPage";
import ExampleComponent from "./ExampleComponent";

const App = () => {
    return (
        <BrowserRouter>
            <NavBar />
            <Routes>
                <Route exact path="/" element={<OrdersPage />} />
                <Route path="/orders" element={<OrdersPage />} />
                <Route path="/menu" element={<MenuPage />} />
                <Route path="/test" element={<ExampleComponent />} />

            </Routes>
        </BrowserRouter>
    );
};

export default App;
