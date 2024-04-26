import Image from "next/image";
import Link from 'next/link';

interface datatype {
    imgSrc: string;
    heading: string;
    paragraph: string;
}

const Aboutdata: datatype[] = [
    {
        imgSrc: "/assets/features/time.svg",
        heading: "Engaging",
        paragraph: 'Excite students with interactive games and downloadable worksheets, enhancing their learning experience. Our platform fosters engagement and curiosity, providing valuable resources for exploring climate change and the Arctic',
    },
    {
        imgSrc: "/assets/features/signal.svg",
        heading: "Insights",
        paragraph: 'Gain useful insights into each one of your enrolled students like their course completion, test scores, and time spent on each module. With customizable marking guides, teachers can easily evaluate student work and provide targeted feedback.',

    },
    {
        imgSrc: "/assets/features/dollar.svg",
        heading: "100% Free",
        paragraph: 'Our platform is completely free, with no hidden costs or subscription fees. Our goal is to make learning about climate change and the Antarctic accessible to teachers and students across New Zealand.',

    }
]

const Features = () => {
    return (
        <div className="bg-babyblue" id="features">
            <div className="mx-auto max-w-2xl py-20 px-4 sm:px-6 lg:max-w-7xl lg:px-8">
                <h3 className="text-4xl sm:text-5xl font-semibold text-black text-center my-10">Amazing Features.</h3>
                <h5 className="text-black opacity-60 text-lg font-normal text-center">Transform your classroom today with ArcticEd&apos;s innovative platform, enhancing climate education through interactive features. <br /> </h5>

                <div className='grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-x-16 gap-y-4 lg:gap-x-8 mt-10'>
                    {Aboutdata.map((item, i) => (
                        <div key={i} className='bg-white rounded-2xl p-5 featureShadow'>

                            <Image src={item.imgSrc} alt={item.imgSrc} width={55} height={55} className="mb-2" />
                            <h3 className="text-2xl font-semibold text-black mt-5">{item.heading}</h3>
                            <h4 className='text-lg font-normal text-black opacity-50 my-2'>{item.paragraph}</h4>
                            <Link href={'/'} className="text-electricblue text-xl font-medium flex gap-2 pt-10 pb-2">
                                Learn more <Image src="/assets/people/arrow-right.svg" alt="arrow-right" width={24} height={24} />
                            </Link>

                        </div>
                    ))}
                </div>
            </div>
        </div>
    )
}

export default Features;
