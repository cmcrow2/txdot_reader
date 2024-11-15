"use client";
import pdf from "@/public/pdf/spec-book-0924.pdf";

export default function Home() {
  return (
    <div>
      <div className="w-full h-20 border-b-2 border-black align-middle flex items-center">
        <p className="text-xl pl-10">PDF Reader</p>
      </div>
      <div className="flex flex-row h-[calc(100vh-5rem)] w-full">
        <div className="w-[60%] border-r-2 border-black flex items-center justify-center">
          <embed type="application/pdf" src={pdf} className="w-[95%] h-[95%]" />
        </div>
        <div className="w-[40%]">Chatbot View</div>
      </div>
    </div>
  );
}
