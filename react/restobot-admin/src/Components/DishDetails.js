import React, { useEffect, useState } from "react";
import axios from "axios";
import { useParams } from "react-router-dom";
import { Box, Container, Button, TextField, FormControl, InputLabel, Select, MenuItem } from "@mui/material";

function DishDetails() {
  const { dishId } = useParams();
  const [dish, setDish] = useState(null);
  const [isEditMode, setIsEditMode] = useState(false);
  const [formData, setFormData] = useState({
    restaurant: 1,
    name: "",
    description: "",
    price: "",
    group: "",
    picture: null,
  });
  const [groups, setGroups] = useState([]);

  useEffect(() => {
    async function fetchDishDetails() {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/dish/get/${dishId}`);
        setDish(response.data);
        setFormData({
          restaurant: 1,
          name: response.data.name,
          description: response.data.description,
          price: response.data.price,
          group: response.data.group,
          picture: null,
        });
      } catch (error) {
        console.error("Error fetching dish details:", error);
      }
    }

    async function fetchGroups() {
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/groups/1");
        setGroups(response.data);
      } catch (error) {
        console.error("Error fetching groups:", error);
      }
    }

    fetchDishDetails();
    fetchGroups();
  }, [dishId]);

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setFormData((prevFormData) => ({
      ...prevFormData,
      [name]: name === "price" ? parseFloat(value) : value,
    }));
  };

  const handleFileChange = (event) => {
    setFormData((prevFormData) => ({
      ...prevFormData,
      picture: event.target.files[0],
    }));
  };

  const handleEditClick = () => {
    setIsEditMode(true);
  };

  const handleCancelClick = () => {
    setIsEditMode(false);
  };

  const handleUpdate = async () => {
    try {
      const formDataToSend = new FormData();
      formDataToSend.append("restaurant", formData.restaurant);
      formDataToSend.append("name", formData.name);
      formDataToSend.append("description", formData.description);
      formDataToSend.append("price", formData.price);
      formDataToSend.append("group", formData.group.id);
      if (formData.picture) {
        formDataToSend.append("picture", formData.picture);
      }
      const response = await axios.put(`http://127.0.0.1:8000/api/dish/update/${dishId}`, formDataToSend, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      setDish(response.data);
      setIsEditMode(false);
    } catch (error) {
      console.error("Error updating dish:", error);
    }
  };

  const handleDeleteClick = async () => {
    console.log('deleting no:', dishId)
    try {
      const response = await axios.delete(`http://127.0.0.1:8000/api/dish/delete/${dishId}`)
    } catch(error) {
      console.log('Error deleting dish', error)
    }
  }

  if (!dish || !groups) {
    return <div>Loading...</div>;
  }

  return (
    <Container maxWidth="sm">
      <Box sx={{ display: "flex", flexDirection: "column", alignItems: "center", mt: 3 }}>
        <h3>Dish Details</h3>
        <TextField
          fullWidth
          label="Name"
          variant="standard"
          name="name"
          value={isEditMode ? formData.name : dish.name}
          onChange={handleInputChange}
          disabled={!isEditMode}
        />
        <TextField
          fullWidth
          label="Description"
          variant="standard"
          name="description"
          multiline
          rows={4}
          value={isEditMode ? formData.description : dish.description}
          onChange={handleInputChange}
          disabled={!isEditMode}
        />
        <TextField
          fullWidth
          label="Price"
          variant="standard"
          name="price"
          value={isEditMode ? formData.price : dish.price}
          onChange={handleInputChange}
          disabled={!isEditMode}
        />
        <FormControl variant="standard" fullWidth>
          <InputLabel id="dish-group">Group</InputLabel>
          <Select
            labelId="dish-group"
            label="Group"
            value={isEditMode ? formData.group : dish.group}
            onChange={handleInputChange}
            name="group"
            disabled={!isEditMode}
          >
            {groups.map((group) => (
              <MenuItem key={group.id} value={group} selected={dish.group.id === group.id}>
                {group.name}
              </MenuItem>
            ))}
          </Select>
        </FormControl>
        <Box mt={2}>
          {isEditMode ? (
            <div>
              <input type="file" name="picture" onChange={handleFileChange} />
              <Button sx={{m:1}} variant="contained" onClick={handleUpdate}>
                Submit
              </Button>
              <Button variant="contained" onClick={handleCancelClick}>
                Cancel
              </Button>
            </div>
          ) : (
            <Container>
              <Button sx={{m:1}} variant="contained" onClick={handleEditClick}>
                Edit
              </Button>
              <Button sx={{m:1}} variant="outlined" color="error" onClick={handleDeleteClick}>
                Delete
              </Button>
            </Container>

          )}
        </Box>
      </Box>
    </Container>
  );
}

export default DishDetails;
