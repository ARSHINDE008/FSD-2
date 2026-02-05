import Form from './Form'
import { CssBaseline, Box } from '@mui/material'

function App() {
  return (
    <>
      <CssBaseline />
      <Box
        sx={{
          width: '100%',
          minHeight: '100vh',
          display: 'flex',
          justifyContent: 'center', // Horizontal center
          alignItems: 'flex-start',  // Vertical top
          pt: 5,                    // Top spacing
          bgcolor: '#f5f5f5'
        }}
      >
        <Form />
      </Box>
    </>
  )
}

export default App
