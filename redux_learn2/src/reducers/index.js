import counter from './counter';
import loggedReducer from './isLogged';
import { combineReducers } from 'redux';
import counterReducer from './counter';

const allReducers = combineReducers({
    counterReducer,
    loggedReducer
})

export default allReducers;