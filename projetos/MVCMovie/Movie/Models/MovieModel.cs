using System.ComponentModel.DataAnnotations;

namespace Movie.Models
{
    public class MovieModel
    {
        [Key]
        public int Id { get; set; }

        [Required(ErrorMessage = "O campo do titulo e obrigatorio.")]
        public string Titulo { get; set; }
        [Required(ErrorMessage = "O campo do diretor e obrigatorio.")]
        public string Genero { get; set; }
        [Required(ErrorMessage = "O campo do diretor e obrigatorio.")]
        [Display(Name = "Diretor")]
        public string Diretor { get; set; }
        [Required(ErrorMessage = " O campo da data de lanchamento do filme e obrigatorio.")]
        [DataType(DataType.Date)]
        public DateTime Lancamento { get; set; }
    }
}
