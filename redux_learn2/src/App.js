import React from 'react';
import { useSelector,useDispatch } from 'react-redux';
import {increment,decrement} from './actions';

function App() {
  const counter=useSelector(state=>state.counterReducer);
  const isLogged=useSelector(state => state.loggedReducer);
  const dispatch=useDispatch();

  return (
    <div className="App">
      <h1>Counter {counter}</h1>
      <button onClick={()=>dispatch(increment(2))}>+</button>
      <button onClick={()=>dispatch(decrement(2))}>-</button>
    </div>
  );
}

export default App;
