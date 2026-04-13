using Microsoft.EntityFrameworkCore;
using Movie.Models;

namespace Movie.DATA
{
    public class MovieContext : DbContext
    {
        public MovieContext(DbContextOptions<MovieContext> options) : base(options) { }

        public DbSet<MovieModel> Movies { get; set; }  // ← Nome no plural (padrão)
    }
}