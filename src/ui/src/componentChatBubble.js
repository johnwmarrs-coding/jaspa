import React from "react";
import { Box, Paper, Typography } from "@mui/material";

const ChatBubble = ({ message }) => {
  return (
    <Box
      sx={{
        display: "flex",
        justifyContent: message.sender == "Jaspa" ? "flex-start" : "flex-end",
        marginBottom: 1,
      }}
    >
      <Paper
        variant="elevation"
        elevation={3}
        sx={{
          borderRadius: "12px",
          backgroundColor: "#f3f3f3", // You can change this
          maxWidth: "80%",
          padding: "10px 20px",
          margin: "10px 20px",
          wordWrap: "break-word",
          overflowWrap: "break-word",
          whiteSpace: "normal",
        }}
      >
        <Typography variant="body1">{message.message}</Typography>
      </Paper>
    </Box>
  );
};

export default ChatBubble;
