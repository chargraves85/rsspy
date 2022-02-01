import { Link } from 'gatsby'
import React from 'react'

export default function Navbar() {
    return (
        <nav>
            <div className='navbar'>
                <Link to='/'>Home</Link>
                <Link to='/about'>About</Link>        
            </div>
        </nav>
    )
}