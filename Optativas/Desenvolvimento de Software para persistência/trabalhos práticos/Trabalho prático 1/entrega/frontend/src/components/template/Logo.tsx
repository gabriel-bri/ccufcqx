import Link from 'next/link'
import Image from 'next/image'

export default function Logo() {
    return (
        <>
            <Link href="/"className={` flex items-center space-x-2 gap-2`}>
            <Image src="/logo.png" width={50} height={50} alt="Logo"/>
            <h1 className="flex flex-col items-center text-lg leading-5">
                <div className='text-gray-100'>
                EVENT
                <span className='text-blue-500'>
                3
                </span>
                </div>
                <div className='text-gray-100'>DIGITAL</div>
            </h1>
            </Link>
        </>
    )
}