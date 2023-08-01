import React, { useEffect, useState } from 'react';
import SideMenu from './SideMenu';
import '../styles.css';
import MainWindow from './MainWindow';
import OrdersPage from './OrdersPage';
import MenuPage from './MenuPage';
import ExampleComponent from './ExampleComponent';

const App = () => {

  const [page, setPage] = useState('menu')




  return (
    <div className='flex' >
      <SideMenu page={page} setPage={setPage}/>
      <MainWindow page={page}/>
    </div>
  );
};

export default App;