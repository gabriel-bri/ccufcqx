import Link from 'next/link'
import Image from 'next/image'

export default function LogoGrande() {
    return (
        <>
            <Link href="/" className={` flex flex-col items-center gap-2`}>
                <Image src="/logo.png" width={100} height={100} alt="Logo" />
                <h1 className="text-5xl text-gray-100">
                    EVENT<span className='text-blue-500'>3</span> DIGITAL
                </h1>
            </Link>
        </>
    )
}