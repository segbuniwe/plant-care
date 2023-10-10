import "./App.css";
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import SignUpForm from "./SignUpForm";

function App() {
  return (
    <>
      <BrowserRouter>
        <div>
          <Routes>
            {/* <Route exact path="/"></Route> */}
            <Route exact path="/signup" element={<SignUpForm />}></Route>
          </Routes>
        </div>
      </BrowserRouter>
    </>
  );
}

export default App;
