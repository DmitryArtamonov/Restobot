import '../styles.css';
import React from 'react';
import OrdersPage from './OrdersPage';
import MenuPage from './MenuPage';

// 



const MainWindow = ({page}) => {
    // const page = 'menu'

    return (
        <div>
            <p> Main window</p>
            {page==='menu' && <MenuPage/>}
            {page==='orders' && <OrdersPage/>}
        </div>
    )
}


export default MainWindow