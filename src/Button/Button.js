import "./Button.css"
function Button({ title, onClick }) {
    return (
        <div onClick={onClick} className="button">{title}</div>
    )
}
export {Button};