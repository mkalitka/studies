using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using FluentNHibernate.Cfg;
using NHibernate;
using FluentNHibernate.Cfg.Db;
using System.Reflection;

namespace FluentMapping
{
    class Program
    {
        private static ISessionFactory CreateSessionFactory()
        {
            return Fluently.Configure()
                .Database( FluentNHibernate.Cfg.Db.MsSqlConfiguration.MsSql2012.ConnectionString("Server=tcp:SQLSERVERURL,1433;Initial Catalog=Test;Persist Security Info=False;User ID=USERNAME;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;Password=PASSWORD;") )
                .Mappings( m => m.FluentMappings.AddFromAssembly( Assembly.GetExecutingAssembly() ) )
                .BuildSessionFactory();
        }
        static void Main( string[] args )
        {
            ISessionFactory sf = CreateSessionFactory();

            using ( var session = sf.OpenSession() )
            {
                using ( var tx = session.BeginTransaction() )
                {
                    var o = new Osoba { Imie = "Jan", Nazwisko = "Kowalski" };
                    session.Save( o );
                    tx.Commit();
                }

                using ( session.BeginTransaction() )
                {
                    var osoby = session.CreateCriteria( typeof( Osoba ) )
                      .List<Osoba>();

                    foreach ( var o in osoby )
                    {
                        Console.WriteLine( o );
                    }
                }
            }
            Console.ReadLine();
        }
    }
}
