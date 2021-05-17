import React from 'react'
import './App.css';
import "bootstrap/dist/css/bootstrap.min.css";
import Header from './components/layouts/Header';
import {Navbar} from "./components/layouts/Navbar"

export const App = () => {
    return (
        <div className= "App">
            <Header/>
            <Navbar/>
        </div>
    )
}

export default App;