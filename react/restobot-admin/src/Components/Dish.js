import '../styles.css';
import ListItem from '@mui/material/ListItem';

const Dish = (dish) => {
    return (
        <ListItem>
            {dish.name}
        </ListItem>



        // <div className="px-2 grid grid-cols-12 py-3 gap-x-6 text-sky-700 hover:bg-gray-300">
        //     <img className="h-fit" src={dish.picture}></img>
        //     <p className="col-span-6">{dish.name}</p>
        //     <p>{dish.price}</p>
            

        // </div>
    )
}


export default Dish