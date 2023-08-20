import React from "react";
import { useContext, useState, useEffect, useRef } from "react";
import { UserContext } from "./App";
import { Button, Typography } from "@mui/material";
import { TextField } from "@mui/material";
import axios from "axios";

import { config } from "./config";
import { Container, Box } from "@mui/material";
import { TextareaAutosize } from "@mui/material";
import SendIcon from "@mui/icons-material/Send";

import CssBaseline from "@mui/material/CssBaseline";

import { ThreeDots } from "react-loader-spinner";

import ChatBubble from "./componentChatBubble";

const Chat = () => {
  const messagesEndRef = useRef(null);
  const { user, setUser } = useContext(UserContext);
  const [text, setText] = useState("");
  const [messageHistory, setMessageHistory] = useState([]);
  const [isWorking, setIsWorking] = useState(false);
  const [isError, setIsError] = useState(false);
  // const [date, setDate] = useState("MM/DD/YYYY");

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messageHistory]);

  const handleSubmit = async (event) => {
    if (text.trim().length == 0) {
      return;
    }
    let updatedMessages = messageHistory;
    event.preventDefault();
    updatedMessages = [
      ...updatedMessages,
      { message: text, recipient: "Jaspa", sender: user.name },
    ];
    setMessageHistory(updatedMessages);
    setIsWorking(true);
    const postBody = {
      message: text,
    };

    setText("");
    console.log(postBody);

    try {
      const url = config.url.API_URL + "/chat";
      console.log("url: ", url);
      const response = await axios.post(url, postBody, {
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${user.authToken}`,
        },
      });

      console.log(response);

      if (response.status === 200) {
        const message = response.data;

        updatedMessages = [...updatedMessages, message];
        setMessageHistory(updatedMessages);

        // TODO: You will have received a message.
        // 1. Add message to message history (Perhaps limit length)
        // 2. Clear message data from text field
      }
    } catch (error) {
      setIsError(true);
    } finally {
      setIsWorking(false);
    }
  };

  const handleEnterKeyPress = (event) => {
    if (event.key === "Enter") {
      // Call your handler function here
      handleSubmit(event);
    }
  };

  return (
    <Container
      component="main"
      maxWidth="md"
      sx={{
        height: "95vh",
        border: "1px solid #ccc",
        boxShadow: "0px 2px 4px rgba(0, 0, 0, 0.1)",
        borderRadius: "10px",
        padding: 2,
        marginTop: 1,
      }}
    >
      <Box
        sx={{
          margin: 1,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          height: "100%",
        }}
      >
        <img style={{ width: 112, height: 112 }} src="/jaspa2.png"></img>

        <Box
          sx={{
            flexGrow: 1,
            display: "flex",
            width: "100%",
            margin: 1,
            maxHeight: "100%",
            flexDirection: "column",
            overflow: "auto",
          }}
        >
          {messageHistory.length == 0 && (
            <Typography sx={{ textAlign: "center" }}>
              No chats yet. Send a message to get started!
            </Typography>
          )}
          {messageHistory.length > 0 &&
            messageHistory.map((message) => <ChatBubble message={message} />)}

          {isWorking && (
            <ChatBubble
              message={{
                sender: "Jaspa",
                message: <ThreeDots height={24} width={24} color="black" />,
                recipient: user.name,
              }}
            />
          )}
          <div ref={messagesEndRef}></div>
        </Box>

        <Box
          width="100%"
          sx={{
            marginTop: 1,
            marginBottom: 1,
            display: "flex",
            flexDirection: "row",
            alignItems: "center",
          }}
        >
          <TextField
            label="Type your message here..."
            onChange={(event) => {
              setText(event.target.value);
            }}
            onKeyDown={handleEnterKeyPress}
            sx={{ flexGrow: 1 }}
            autoFocus
            value={text}
          ></TextField>
          <Button
            variant="outlined"
            onClick={handleSubmit}
            color="primary"
            sx={{
              width: 100,
              marginLeft: 1,

              height: 56,
            }}
          >
            <SendIcon />
          </Button>
        </Box>
      </Box>
    </Container>
  );
};

export default Chat;
