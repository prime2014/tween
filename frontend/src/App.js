import { BrowserRouter, Route, Routes } from "react-router-dom";
import Home from "./Components/Home/Home";


function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <Routes>
          <Route path={"/"} element={<Home />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
