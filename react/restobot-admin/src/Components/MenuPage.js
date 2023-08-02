import React, { useEffect, useState } from "react";
import { DataGrid } from "@mui/x-data-grid";

const columns = [
    {
        field: "picture",
        headerName: "",
        width: 70,
        minWidth: 70,
        renderCell: (params) => <img src={params.value} width={50} />,
    },
    {
        field: "group",
        headerName: "Group",
        flex: 2,
        minWidth: 100,
        renderCell: (params) => (params.value ? params.value.name : null),
    },
    { field: "name", headerName: "Name", flex: 5, minWidth: 100 },
    {
        field: "price",
        headerName: "Price",
        type: "number",
        flex: 2,
        minWdth: 70,
    },
];

function MenuPage() {
    const [dishes, setDishes] = useState([]);

    useEffect(() => {
        // Create an asynchronous function to perform the GET request
        async function fetchDishes() {
            try {
                // Await the completion of the GET request and get the response
                const response = await fetch(
                    "http://127.0.0.1:8000/api/dishes/1"
                );
                const data = await response.json();
                // Update the 'dishes' state with the received data
                setDishes(data);
            } catch (error) {
                console.error("Error fetching dishes:", error);
            }
        }

        // Call the asynchronous function to perform the GET request
        fetchDishes();
    }, []);

    console.log(dishes);

    return (
        <div style={{ height: 400, width: "100%" }}>
            <DataGrid
                rows={dishes}
                columns={columns}
                initialState={{
                    pagination: {
                        paginationModel: { page: 0, pageSize: 5 },
                    },
                }}
                pageSizeOptions={[20, 50, 100]}
                checkboxSelection
            />
        </div>
    );
}

export default MenuPage;
