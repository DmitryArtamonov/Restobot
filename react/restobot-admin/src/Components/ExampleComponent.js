import Box from "@mui/material/Box";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import { FormControl, FormLabel } from "@mui/material";



function ExampleComponent() {
    return (
        <Box
            component="form"
            sx={{
                "& .MuiTextField-root": {
                    m: 1,
                    width: "50ch",
                    display: "flex",
                    flexDirection: "column",
                },
            }}
        >
            <TextField
                id="name"
                label="Name"
                required
                fullWidth
                variant="standard"
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
            />
            <TextField
                id="price"
                label="Price"
                required
                fullWidth
                variant="standard"
            />

            <Button>Submit</Button>
        </Box>
    );
}

export default ExampleComponent;
