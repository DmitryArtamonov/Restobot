import '../styles.css';
import OrdersPage from './OrdersPage';
import MenuPage from './MenuPage';
import { Button } from '@mui/material';


const SideMenu = ({page, setPage}) => {



    return (
        <div>
            <Button onClick={() => setPage('orders')}>Orders</Button>
            <Button onClick={() => setPage('menu')}>Menu</Button>
            <Button onClick={() => setPage('test')}>Test</Button>
        </div>
    )
}


export default SideMenu