%include	/usr/lib/rpm/macros.perl
%define	pdir	Config
%define	pnam	Reader
Summary:	ConfigReader -- Read directives from a configuration file.
Summary(pl):	ConfigReader -- czytaj dyrektywy z pliku konfiguracyjnego.
Name:		perl-ConfigReader
Version:	0.5
Release:	3
License:	LGPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ConfigReader is a set of classes for reading configuration files.
The programmer can easily specify the directives to be read, as well as
their default values and a parsing function or method to use.  A lot of
work went into error handling.

%description -l pl
ConfigReader jest zbiorem klas, s³u¿±cych do czytania plików
konfiguracyjnych.  Programista mo¿e w prosty sposób wskazaæ dyrektywy do
przeczytania, ich domy¶lne warto¶ci i funkcjê, któr± nale¿y zastosowaæ
do sprawdzania sk³adni.

%prep
%setup -q -n %{pdir}%{pnam}-%{version}

%build
echo 'use ExtUtils::MakeMaker; WriteMakefile(VERSION_FROM=>"Spec.pm",
      NAME=>"ConfigReader::Spec");' > Makefile.PL
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{perl_sitelib}/ConfigReader
%{perl_sitelib}/ConfigReader/*.pm
%{_mandir}/man3/*
