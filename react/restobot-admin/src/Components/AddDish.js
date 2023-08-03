import React, { useEffect, useState } from "react";
import axios from "axios";

import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import TextField from "@mui/material/TextField";
import InputLabel from "@mui/material/InputLabel";
import Select from "@mui/material/Select";
import MenuItem from "@mui/material/MenuItem";
import Button from "@mui/material/Button";
import { FormControl, FormLabel } from "@mui/material";

import fetchApi from "../utils/fetch-api";

function ExampleComponent() {
  const [groups, setGroups] = useState([]);
  const [formData, setFormData] = useState({
    name: "",
    description: "",
    price: "",
    group: "",
    restaurant: 1,
    picture: null, // Added a new state to store the selected picture file
  });

  useEffect(() => {
    async function fetchGroups() {
      const data = await fetchApi("groups/1");
      setGroups(data);
    }
    fetchGroups();
  }, []);

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
      picture: event.target.files[0], // Save the selected picture file in the state
    }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const formDataToSend = new FormData();
      formDataToSend.append("name", formData.name);
      formDataToSend.append("description", formData.description);
      formDataToSend.append("price", formData.price);
      formDataToSend.append("group", formData.group);
      formDataToSend.append("restaurant", formData.restaurant);
      if (formData.picture) {
      formDataToSend.append("picture", formData.picture); // Append the picture file to FormData
      }

      const response = await axios.post(
        "http://127.0.0.1:8000/api/dish/new",
        formDataToSend,
        {
          headers: {
            "Content-Type": "multipart/form-data", // Set the correct content type for form data
          },
        }
      );
      console.log("Response:", response.data);
      // Handle the response data here
    } catch (error) {
      console.error("Error:", error);
      // Handle the error here
    }
    console.log(formData);
  };

  return (
    <Container sx={{ display: "flex", width: "50ch" }}>
      <Box
        component="form"
        onSubmit={handleSubmit} // Add onSubmit handler to the form
        sx={{
          "& .MuiTextField-root": {
            m: 1,
            width: "50ch",
            display: "flex",
            flexDirection: "column",
          },
        }}
      >
        <Container>
          <h3>Create new dish</h3>

          <TextField
            id="name"
            label="Name"
            required
            fullWidth
            variant="standard"
            name="name" // Add name attribute to the input field
            value={formData.name} // Set value to the formData state
            onChange={handleInputChange}
          />
          <TextField
            id="description"
            label="Description"
            placeholder="Сomposition of the dish, calories, etc."
            variant="standard"
            fullWidth
            required
            multiline
            rows={4}
            name="description" // Add name attribute to the input field
            value={formData.description} // Set value to the formData state
            onChange={handleInputChange}
          />
          <TextField
            id="price"
            label="Price"
            required
            fullWidth
            variant="standard"
            name="price" // Add name attribute to the input field
            inputProps={{ inputMode: 'numeric', pattern: '[0-9]*' }}
            value={formData.price} // Set value to the formData state
            onChange={handleInputChange}
          />
          <FormControl variant="standard" sx={{ width: "50ch", m: 1 }}>
            <InputLabel id="dish-group">Group</InputLabel>
            <Select
              fullWidth
              labelId="dish-group"
              id="group"
              label="Group"
              value={formData.group} // Set value to the formData state
              onChange={handleInputChange}
              name="group" // Add name attribute to the input field
            >
              {groups ? (
                groups.map((group) => (
                  <MenuItem key={group.id} value={group.id}>
                    {group.name}
                  </MenuItem>
                ))
              ) : (
                <MenuItem value=""> </MenuItem>
              )}
            </Select>
          </FormControl>

          <input
            type="file" // Add a file input to allow picture uploads
            name="picture"
            onChange={handleFileChange} // Set the handler for when a file is selected
          />
        </Container>

        <Container sx={{ display: "flex", justifyContent: "flex-end" }}>
          <Button type="submit">Submit</Button>
        </Container>
      </Box>
    </Container>
  );
}

export default ExampleComponent;
