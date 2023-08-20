import * as React from "react";
import Avatar from "@mui/material/Avatar";
import Button from "@mui/material/Button";
import CssBaseline from "@mui/material/CssBaseline";
import TextField from "@mui/material/TextField";
import FormControlLabel from "@mui/material/FormControlLabel";
import Checkbox from "@mui/material/Checkbox";
import Link from "@mui/material/Link";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import LockOutlinedIcon from "@mui/icons-material/LockOutlined";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import { createTheme, ThemeProvider } from "@mui/material/styles";

import { DatePicker } from "@mui/x-date-pickers/DatePicker";

import { useState, useContext } from "react";
import { UserContext } from "./App";

import { config } from "./config";

import axios from "axios";
import moment from "moment";

const defaultTheme = createTheme();

export default function SignIn() {
  const { user, setUser } = useContext(UserContext);
  const [isWorking, setIsWorking] = useState(false);
  const [isInvalid, setIsInvalid] = useState(false);
  const [date, setDate] = useState(null);

  const handleSubmit = async (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    const postBody = {
      password: data.get("motto"),
      first_date_password: date.format("MM/DD/YYYY").toString(),
      user_password: data.get("animal"),
    };
    console.log(postBody);

    setIsWorking(true);

    try {
      const url = config.url.API_URL + "/authenticate";
      console.log("url: ", url);
      const response = await axios.post(url, postBody, {
        headers: { "Content-Type": "application/json" },
      });

      if (response.status === 200) {
        setUser({
          authToken: response.data.token,
          name: response.user,
          loggedIn: true,
        });
      }
    } catch (error) {
      console.log("error");
      setIsInvalid(true);
    } finally {
      setIsWorking(false);
    }
  };

  const [code, setCode] = useState("");

  return (
    <ThemeProvider theme={defaultTheme}>
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <Box
          sx={{
            marginTop: 8,
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
          }}
        >
          <img style={{ width: 56, height: 56 }} src="/jaspa_favicon.png"></img>
          <Typography component="h1" variant="h5">
            Sign in
          </Typography>
          <Box
            component="form"
            onSubmit={handleSubmit}
            noValidate
            sx={{ mt: 1 }}
          >
            <TextField
              margin="normal"
              required
              fullWidth
              name="motto"
              label="motto"
              id="motto"
            ></TextField>
            <DatePicker
              name="date"
              label="date *"
              id="date"
              value={date}
              onChange={(value) => {
                setDate(value);
              }}
              sx={{ width: "100%" }}
            />
            <TextField
              margin="normal"
              required
              fullWidth
              name="animal"
              label="Favorite Animal"
              id="animal"
            />
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
            >
              Submit
            </Button>
          </Box>
        </Box>
      </Container>
    </ThemeProvider>
  );
}
