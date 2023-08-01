import '../styles.css';
import OrdersPage from './OrdersPage';
import MenuPage from './MenuPage';


const SideMenu = ({page, setPage}) => {



    return (
        <div>
            <p id='orders' onClick={() => setPage('orders')}>Orders</p>
            <p id='menu' onClick={() => setPage('menu')}>Menu</p>
        </div>
    )
}


export default SideMenu