import EmojiPicker from "emoji-picker-react";
import { useState } from "react";
import TextField from "@mui/material/TextField";
import InputEmoji from "react-input-emoji";

const EmojiInput = ({ text, setText }) => {
  const [isFocused, setIsFocused] = useState(true);
  return (
    <div>
      <TextField
        margin="normal"
        required
        fullWidth
        id="code"
        label="code"
        name="code"
        autoFocus
        value={text}
        onFocus={(e) => {
          setIsFocused(true);
          console.log("Weyo");
        }}
        onBlur={(e) => {
          setIsFocused(false);
          console.log("Blurred");
        }}
        onChange={(e) => {
          setText(e.target.value);
        }}
      ></TextField>

      <EmojiPicker
        onEmojiClick={(emojiObject) => setText(text + emojiObject.emoji)}
        skinTonesDisabled={true}
      />
    </div>
  );
};

export default EmojiInput;
