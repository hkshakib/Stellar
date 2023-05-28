import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './Containers/Home';
import About from './Containers/About';
import Contact from './Containers/Contact';
import Listings from './Containers/Listings';
import Login from './Containers/Login';
import SignUp from './Containers/SignUp';
import NotFound from './Containers/NotFound';
import Layout from './Hocs/Layout';


const App = () => (
        <Router>
            <Layout>
                <Routes>
                    <Route path='/' element={<Home />} />
                    <Route path='/about' element={<About />} />
                    <Route path='/contact' element={<Contact />} />
                    <Route path='/listings' element={<Listings />} />
                    <Route path='/login' element={<Login />} />
                    <Route path='/signup' element={<SignUp />} />
                    <Route path='*' element={<NotFound />} />
                </Routes>
            </Layout>
        </Router>
);

export default App;
