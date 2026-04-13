using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using System;
using Movie.DATA;
using Movie.Models;

namespace Movie.Controllers
{
    public class MovieController : Controller
    {
        private readonly MovieContext _context;

        public MovieController(MovieContext context)
        {
            _context = context;
        }

        // LISTAR TODOS
        public async Task<IActionResult> Index()
        {
            var lista = await _context.Movies.ToListAsync();
            return View(lista);
        }

        // BUSCAR
        // BUSCAR - CORREÇÃO 4
        public async Task<IActionResult> Pesquisar(string titulo, string genero)
        {
            var filme = from m in _context.Movies select m;

            if (!string.IsNullOrEmpty(titulo))
            {
                filme = filme.Where(m => m.Titulo.Contains(titulo));
            }

            if (!string.IsNullOrEmpty(genero))
            {
                filme = filme.Where(m => m.Genero.Contains(genero));
            }

            ViewData["titulo"] = titulo;

            var resultado = await filme.ToListAsync();
            return View("Index", resultado);  // ← Volta para Index com os resultados
        }

        // CREATE (GET) - Mostrar formulário
        [HttpGet]
        public IActionResult Adicionar()
        {
            return View();
        }

        // CREATE (POST) - Salvar no banco
        [HttpPost]
        public async Task<IActionResult> Adicionar(MovieModel filme)
        {
            if (ModelState.IsValid)
            {
                _context.Movies.Add(filme);
                await _context.SaveChangesAsync();
                return RedirectToAction("Index");
            }

            return View(filme);
        }

        // EDIT (GET) - Mostrar formulário com dados
        [HttpGet]
        public async Task<IActionResult> Editar(int id)
        {
            var filme = await _context.Movies.FindAsync(id);

            if (filme == null)
            {
                return NotFound(id);
            }

            return View(filme);
        }

        // EDIT (POST) - Salvar alterações
        [HttpPost]
        public async Task<IActionResult> Editar(int id, MovieModel filme)
        {
            if (id != filme.Id)
            {
                return NotFound();
            }

            if (ModelState.IsValid)
            {
                _context.Movies.Update(filme);
                await _context.SaveChangesAsync();
                return RedirectToAction("Index");
            }

            return View(filme);
        }

        // ========== DELETE (GET) - CORRETO ==========
        [HttpGet]
        public async Task<IActionResult> Excluir(int id)  // ← CORRIGIDO: Nome maiúsculo
        {
            try
            {
                var filme = await _context.Movies.FindAsync(id);

                if (filme == null)
                {
                    return NotFound();
                }

                return View(filme);
            }
            catch (Exception ex) {  // ← CORRIGIDO: Sem ponto e vírgula!
                {
                    return View("Error");
                }
            }
        }

        // ⚠️ Só use em desenvolvimento/teste, NUNCA em produção!

        [HttpPost, ActionName("Excluir")]
        public async Task<IActionResult> ExcluirConfirmado(int id)
        {
            try
            {
                var filme = await _context.Movies.FindAsync(id);

                if (filme == null)
                {
                    return NotFound();
                }

                _context.Movies.Remove(filme);
                await _context.SaveChangesAsync();

                // ⚠️ Se não tiver mais nenhum filme, reinicia a contagem
                if (!_context.Movies.Any())
                {
                    await _context.Database.ExecuteSqlRawAsync("DBCC CHECKIDENT ('Movies', RESEED, 0)");
                }

                return RedirectToAction("Index");
            }
            catch (Exception ex)
            {
                return View("Error");
            }
        }
         }
    }
