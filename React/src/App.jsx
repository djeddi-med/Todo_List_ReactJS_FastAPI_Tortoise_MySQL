import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';
import Header from "./components/Header";
import Form from './components/Form';
import TodoList from './components/TodoList';



function App() {
  const url = 'http://127.0.0.1:8000';
  const [input, setInput] = useState('');
  const  [todos, setTodos] = useState([]);
  const [editTodo, setEditTodo] = useState(null);
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    // Fetch data from the local server (localhost:8000)
    fetch('http://localhost:8000') // Assuming your server endpoint is /tasks
      .then(response => response.json())
      .then(data => setTasks(data))
      .catch(error => console.error('Erreur ...:', error)) 
  }, []);
  





  return (
    <center>
      <div className='container'>
        <div className='app-wrapper'>
          <div>
            <Header />
          </div>
          <div>
            <Form
              input={input}
              setInput={setInput}
              todos={todos}
              setTodos={setTodos}
              editTodo={editTodo}
              setEditTodo={setEditTodo}

            />
          </div>
          <div>
            <TodoList todos={todos} setTodos={setTodos} setEditTodo={setEditTodo}  />
          </div>

        </div>


        <div>

        
      
        </div>

      </div>
    </center>
  );
}

export default App;