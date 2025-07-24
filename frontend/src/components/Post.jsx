
import CommentBox from './CommentBox';

function Post() {
  return (
    <div className="w-11/12 max-w-xl mx-auto my-8 border border-gray-300 rounded-2xl overflow-hidden bg-white shadow">
      <div className="w-full bg-gray-100 text-center py-12 text-gray-500 text-lg">
        📷 Imagen de muestra aquí
      </div>
      <div className="p-4 space-y-2">
        <div className="rounded-xl p-3 bg-red-50 text-gray-800">❤️ ¡Qué buena está esta cerveza!</div>
        <div className="rounded-xl p-3 bg-blue-50 text-gray-800">👍 Me encantó esta receta azul cielo</div>
        <div className="rounded-xl p-3 bg-yellow-100 text-gray-800">🏅 Esta es digna de premiación</div>
        <CommentBox />
      </div>
      <div className="text-right text-xs text-gray-500 px-3 py-2 border-t border-gray-200 bg-gray-50">
        ¡Gánatelo! Próximamente disponible
      </div>
    </div>
  );
}

export default Post;
