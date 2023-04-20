import React from 'react';


const Header = () => {
    return (
        <div className="w-screen  h-[80px] z-10 bg-blue-300 fixed drop-shadow-md">
            <div className="px-2 flex justify-between items-center w-full h-full">
                <div>
                    <h1 className="text-3xl font-bold mr-4">Row Reduction Calculator</h1>
                </div>
            </div>
        </div>
    )

}

export default Header;
