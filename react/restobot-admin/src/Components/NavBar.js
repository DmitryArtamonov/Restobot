import { Link } from "react-router-dom";
import { Button } from "@mui/material";

const NavBar = () => {
    return (
        <div>
            <Link to="/">
                <Button>Home</Button>
            </Link>
            <Link to="/orders">
                <Button>Orders</Button>
            </Link>
            <Link to="/menu">
                <Button>Menu</Button>
            </Link>
            <Link to="/test">
                <Button>TEST</Button>
            </Link>
        </div>
    );
};

export default NavBar;
