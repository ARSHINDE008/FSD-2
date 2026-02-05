import {
  TextField,
  Button,
  Container,
  Typography,
  Checkbox,
  FormControlLabel,
  Radio,
  RadioGroup,
  FormControl,
  FormLabel,
  Box
} from '@mui/material';
import { useState } from 'react';

export default function Form() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [rememberMe, setRememberMe] = useState(false);
  const [gender, setGender] = useState('female');
  const [errors, setErrors] = useState({});

  const validate = () => {
    let temp = {};
    // Name validation
    if (!name) {
      temp.name = "Name is required";
    }

    // Email basic validation
    if (!email) {
      temp.email = "Email is required";
    } else if (!/\S+@\S+\.\S+/.test(email)) {
      temp.email = "Email is invalid";
    }

    // Password validation (as per teacher snippet)
    if (password.length < 6) {
      temp.password = 'Min 6 characters';
    }

    setErrors(temp);
    return Object.keys(temp).length === 0;
  }

  const handleSubmit = (e) => {
    e.preventDefault();

    // Check validity of browser-level validations (required, type="email", minLength)
    if (e.target.checkValidity() && validate()) {
      alert('Form submitted successfully!\n' + JSON.stringify({ name, email, password, rememberMe, gender }, null, 2));
    } else {
      console.log("Validation failed");
    }
  }

  return (
    <Container maxWidth="sm" sx={{
      mt: 4,
      p: 3,
      boxShadow: 3,
      borderRadius: 2,
      bgcolor: 'background.paper',
      display: 'flex',
      flexDirection: 'column',
      justifyContent: 'center'
    }}>
      <Typography variant="h4" gutterBottom align="center" color="primary">
        User Registration
      </Typography>

      <form onSubmit={handleSubmit} noValidate>
        <TextField
          type="text"
          value={name}
          required
          onChange={e => setName(e.target.value)}
          label="Full Name"
          fullWidth
          margin="normal"
          error={Boolean(errors.name)}
          helperText={errors.name}
        />

        <TextField
          type="email"
          value={email}
          required
          onChange={e => setEmail(e.target.value)}
          label="Email Address"
          fullWidth
          margin="normal"
          error={Boolean(errors.email)}
          helperText={errors.email}
        />

        <TextField
          type="password"
          value={password}
          required
          onChange={e => setPassword(e.target.value)}
          label="Password"
          fullWidth
          margin="normal"
          inputProps={{ minLength: 5 }}
          error={Boolean(errors.password)}
          helperText={errors.password}
        />

        <FormControl component="fieldset" margin="normal" fullWidth>
          <FormLabel component="legend">Gender</FormLabel>
          <RadioGroup
            row
            aria-label="gender"
            name="gender"
            value={gender}
            onChange={e => setGender(e.target.value)}
          >
            <FormControlLabel value="female" control={<Radio />} label="Female" />
            <FormControlLabel value="male" control={<Radio />} label="Male" />
            <FormControlLabel value="other" control={<Radio />} label="Other" />
          </RadioGroup>
        </FormControl>

        <FormControlLabel
          control={
            <Checkbox
              checked={rememberMe}
              onChange={e => setRememberMe(e.target.checked)}
              color="primary"
            />
          }
          label="I agree to the terms and conditions"
        />

        <Box sx={{ mt: 3 }}>
          <Button
            variant="contained"
            type="submit"
            fullWidth
            size="large"
            sx={{ py: 1.5 }}
          >
            Submit Application
          </Button>
        </Box>
      </form>
    </Container>
  );
}
