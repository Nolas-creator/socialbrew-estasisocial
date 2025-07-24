
import { useState } from 'react';

function CommentBox() {
  const [showInput, setShowInput] = useState(false);
  const [text, setText] = useState('');

  const toggleInput = () => setShowInput(!showInput);

  return (
    <div className="mt-4">
      <button
        onClick={toggleInput}
        className="flex items-center gap-2 text-blue-700 hover:text-blue-900 text-sm"
      >
        <span className="text-lg">💭🕶️</span>
        <span>Comenta con sabiduría</span>
      </button>
      {showInput && (
        <div className="mt-2">
          <textarea
            value={text}
            onChange={(e) => setText(e.target.value)}
            className="w-full border rounded-lg p-2 text-sm"
            placeholder="Escribe tu comentario aquí..."
          />
          <button className="mt-2 bg-yellow-500 text-white px-3 py-1 rounded hover:bg-yellow-600">
            Enviar
          </button>
        </div>
      )}
    </div>
  );
}

export default CommentBox;
