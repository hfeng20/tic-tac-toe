import logo from './logo.svg';
import './App.css';
import {Button} from './Button/Button';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>Hello</code> and save to reload.
        </p>
        <Button title="Khan Academy" onClick={() => window.open("https://www.khanacademy.org/", "_blank")} />
        <Button title="Youtube" onClick={() => window.open("https://www.youtube.com", "_blank")} />
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
