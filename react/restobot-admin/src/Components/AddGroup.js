import React, { useRef } from "react";
import { Box, TextField } from "@mui/material";
import DoneIcon from "@mui/icons-material/Done";
import CloseIcon from "@mui/icons-material/Close";
import axios from "axios";

export const AddGroup = (props) => {
    const { addCategory, setAddCategory } = props;
    const groupNameRef = useRef('');
  
    const addNewCategory = async () => {
      try {
        // Access the input value using the ref
        const groupName = groupNameRef.current.value;
        if (groupName) {
        const response = await axios.post(
          "http://127.0.0.1:8000/api/groups/new",
          { name: groupName, restaurant: 1 }
        );
  
        // Clear the field after successful addition
        groupNameRef.current.value = '';
      }} catch (error) {
        console.error("Error adding new group:", error);
      }
    };

  return (
    <Box sx={{ display: "flex", justifyContent: "flex-end", alignItems: 'center'}}>
      <TextField
        size="small"
        margin="dense"
        label="Group Name"
        variant="standard"
        name="group-name"
        inputRef={groupNameRef} // Assign the ref to the input element
      />
      <DoneIcon
        fontSize="small"
        sx={{ m: 1 }}
        color="primary"
        onClick={addNewCategory}
      />
      <CloseIcon
        fontSize="small"
        sx={{ m: 1 }}
        color="error"
        onClick={() => setAddCategory(false)}
      />
    </Box>
  );
};
