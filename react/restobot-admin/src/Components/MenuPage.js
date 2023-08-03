import React, { useEffect, useState } from "react";
import { DataGrid } from "@mui/x-data-grid";
import { Container, Button } from "@mui/material";
import { Link } from "react-router-dom";
import fetchApi from "../utils/fetch-api";

import { AddGroup } from "./AddGroup";

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
    {
        field: "name",
        headerName: "Name",
        flex: 5,
        minWidth: 100,
        renderCell: (params) => (
            <Link to={"/dish/" + params.row.id}>{params.row.name}</Link>
        ),
    },
    {
        field: "price",
        headerName: "Price",
        type: "number",
        flex: 2,
        minWdth: 70,
    },
];

function MenuPage() {
    const [dishes, setDishes] = useState();
    const [addCategory, setAddCategory] = useState(false);

    useEffect(() => {
        async function fetchDishes() {
            const data = await fetchApi("dishes/1");
            setDishes(data);
        }
        fetchDishes();
    }, []);

    return (
        <div style={{ height: 400, width: "100%" }}>
            <h3>Menu Page</h3>
            <Container sx={{ display: "flex", justifyContent: "flex-end" }}>
                <Link to="/add-dish">
                    <Button sx={{ m: 1, mr: 0 }} variant="outlined">
                        + Dish
                    </Button>
                </Link>
                <Button
                    sx={{ m: 1, mr: 0 }}
                    variant="outlined"
                    onClick={() => setAddCategory(!addCategory)}
                >
                    + Group
                </Button>
            </Container>

            {addCategory && (
                <Container >
                    <AddGroup
                        addCategory={addCategory}
                        setAddCategory={setAddCategory}
                    />
                </Container>
            )}

            {dishes ? (
                <DataGrid
                    rows={dishes}
                    columns={columns}
                    initialState={{
                        pagination: {
                            paginationModel: { page: 0, pageSize: 20 },
                        },
                    }}
                    pageSizeOptions={[20, 50, 100]}
                    checkboxSelection
                />
            ) : (
                <p>Loading...</p>
            )}
        </div>
    );
}

export default MenuPage;
