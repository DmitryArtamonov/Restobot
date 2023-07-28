// import './Dish.css'
import './styles.css';


const Dish = (dish) => {
    console.log(dish)
    return (
        <div className="flex justify-between gap-x-6 py-5">
            <p>{dish.name}</p>
            <p>{dish.price}</p>
            

        </div>
    )
}


export default Dish