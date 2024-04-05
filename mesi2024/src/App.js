import React from 'react';
import Accueil from './Acceuil';
import Navbar from './Navbar';
import MovieInfo from './MovieInfo';
import ActionButtons from './ActionButtons';
import './App.css';

const App = () => {
  return (
    <div className="App">
     <Navbar />
      <Accueil />
      <MovieInfo />
      <ActionButtons />
    </div>
  );
}

export default App;

