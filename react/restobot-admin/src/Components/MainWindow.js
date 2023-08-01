import '../styles.css';
import React from 'react';
import OrdersPage from './OrdersPage';
import MenuPage from './MenuPage';
import Button from '@mui/material/Button';
import ExampleComponent from './ExampleComponent';

// 



const MainWindow = ({page}) => {
    // const page = 'menu'

    return (
        <div>
            <h1> Main window</h1>
            {page==='menu' && <MenuPage/>}
            {page==='orders' && <OrdersPage/>}
            {page==='test' && <ExampleComponent/>}
            
        </div>
    )
}


export default MainWindow